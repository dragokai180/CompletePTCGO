from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from spirit.game.card_effects.attacks_common import damage_per, count_energy
from spirit.game.card_effects.pokemon import TeraRulePassive
from spirit.game.card_effects.trainers import is_basic_energy_card


def _is_basic_grass_energy(card) -> bool:
    types = card.get_attribute(AttrID.POKEMON_TYPES) or []
    return is_basic_energy_card(card) and PokemonTypes.GRASS.value in types


def _teal_dance_condition(board, player_id, pokemon) -> bool:
    hand = board.find_player_area(player_id, "hand")
    return bool(hand and any(_is_basic_grass_energy(c) for c in hand.children))


async def teal_dance(ctx):
    """Attach a Basic Grass Energy from your hand to this Pokemon; if you
    did, draw a card."""
    candidates = [c for c in ctx.hand() if _is_basic_grass_energy(c)]
    if not candidates:
        return
    picks = await ctx.choose_cards(
        candidates, 1,
        prompt="Choose a Basic Grass Energy card to attach to this Pokémon.",
    )
    if not picks:
        return
    await ctx.attach_energy(picks[0], ctx.source)
    await ctx.draw_cards(1)


def _energy_on_both_actives(ctx) -> int:
    return count_energy("self")(ctx) + count_energy("defender")(ctx)


card = PokemonCardDef(
    guid="e9dbeff9-d840-51ab-9bcd-05e4e09af0fc",
    key="SV06",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TealMaskOgerponex.Name",
    display_name="Teal Mask Ogerpon ex",
    searchable_by=["Teal Mask Ogerpon ex", "Basic", "ex", "Tera", "TealMaskOgerponex"],
    subtypes=["Basic", "ex", "Tera"],
    collector_number=25,
    set_code="SV06",
    regulation_mark="H",
    rarity=Rarities.RareHoloEX,
    hp=210,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=1017,
    passive=TeraRulePassive(),
    abilities=[
        Ability(
            title="Teal Dance",
            game_text="Once during your turn, you may attach a Basic [G] Energy card from your hand to this Pokémon. If you attached Energy to a Pokémon in this way, draw a card.",
            activation=Activations.ONCE_PER_TURN,
            condition=_teal_dance_condition,
            effect=teal_dance,
        ),
        Attack(
            title="Myriad Leaf Shower",
            game_text="This attack does 30 more damage for each Energy attached to both Active Pokémon.",
            cost={PokemonTypes.GRASS: 3},
            damage=30,
            damage_operator="+",
            effect=damage_per(_energy_on_both_actives, 30, base=30),
        ),
    ],
)
