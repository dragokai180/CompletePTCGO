from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import count_energy, damage_per
from spirit.game.card_effects.trainers import is_basic_energy_card


def _is_basic_grass_energy(card) -> bool:
    return (
        is_basic_energy_card(card)
        and PokemonTypes.GRASS.value in (
            card.get_attribute(AttrID.POKEMON_TYPES) or []
        )
    )


def ripening_charge_condition(board, player_id, pokemon=None) -> bool:
    """The heal is a consequence, not a targeting restriction."""
    hand = board.find_player_area(player_id, "hand")
    return bool(
        board.pokemon_in_play(player_id)
        and hand
        and any(_is_basic_grass_energy(card) for card in hand.children)
    )


async def ripening_charge(ctx):
    energies = [card for card in ctx.hand() if _is_basic_grass_energy(card)]
    if not energies:
        return
    picks = await ctx.choose_cards(
        energies, 1, prompt="Choose a Basic Grass Energy card to attach"
    )
    if not picks:
        return
    target = await ctx.choose_pokemon(
        ctx.my_pokemon_in_play(), "Choose a Pokemon for Ripening Charge"
    )
    if target is None:
        return
    if await ctx.attach_energy(picks[0], target, counts_as_attachment=True):
        await ctx.heal(30, target)


syrup_storm = damage_per(
    count_energy("mine", energy_type=PokemonTypes.GRASS),
    per=30,
    base=30,
)


card = PokemonCardDef(
    guid="4aac6eeb-6e65-5cfe-a1a1-d779f10c79e5",
    key="SV07",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hydrappleex.Name",
    display_name="Hydrapple ex",
    searchable_by=["Hydrapple ex", "Stage 2", "ex", "Hydrappleex"],
    subtypes=["Stage 2", "ex"],
    collector_number=14,
    set_code="SV07",
    regulation_mark="H",
    rarity=Rarities.RareHoloEX,
    hp=330,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Dipplin.Name",
    family_id=840,
    abilities=[
        Ability(
            title="Ripening Charge",
            game_text="Once during your turn, you may attach a Basic Grass Energy card from your hand to 1 of your Pokémon. If you attached Energy to a Pokémon in this way, heal 30 damage from that Pokémon.",
            effect=ripening_charge,
            condition=ripening_charge_condition,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title="Syrup Storm",
            game_text="This attack does 30 more damage for each Grass Energy attached to all of your Pokémon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="+",
            effect=syrup_storm,
        ),
    ],
)
