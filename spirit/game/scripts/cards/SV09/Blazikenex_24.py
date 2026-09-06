from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import lock_all_attacks
from spirit.game.card_effects.support_common import attach_from_discard, requires_discard
from spirit.game.card_effects.trainers import is_basic_energy_card


seething_spirit = attach_from_discard(
    predicate=is_basic_energy_card, count=1, target="choice",
    prompt="Choose a Basic Energy card to attach.",
)


async def smolder_sault(ctx):
    """200. During your next turn, this Pokémon can't attack."""
    await ctx.deal_damage()
    lock_all_attacks(ctx, ctx.attacker)


card = PokemonCardDef(
    guid="4d0771bd-0d12-5569-ad70-89b54168b209",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Blazikenex.Name",
    display_name="Blaziken ex",
    searchable_by=["Blaziken ex", "Stage 2", "ex", "Blazikenex"],
    subtypes=["Stage 2", "ex"],
    collector_number=24,
    set_code="SV09",
    regulation_mark="H",
    rarity=Rarities.RareHoloEX,
    hp=320,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Combusken.Name",
    family_id=255,
    abilities=[
        Ability(
            title="Seething Spirit",
            game_text="Once during your turn, you may attach a Basic Energy card from your discard pile to 1 of your Pokémon.",
            activation=Activations.ONCE_PER_TURN,
            condition=requires_discard(is_basic_energy_card),
            effect=seething_spirit,
        ),
        Attack(
            title="Smolder-sault",
            game_text="During your next turn, this Pokémon can't attack.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=200,
            effect=smolder_sault,
        ),
    ],
)
