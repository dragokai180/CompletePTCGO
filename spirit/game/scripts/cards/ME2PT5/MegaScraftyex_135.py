from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="e871fd1c-6813-5b9e-9769-abce78383803",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MegaScraftyex.Name",
    display_name="Mega Scrafty ex",
    searchable_by=["Mega Scrafty ex", "Stage 1", "MEGA", "ex", "SV_Mega", "MegaScraftyex"],
    subtypes=["Stage 1", "MEGA", "ex", "SV_Mega"],
    collector_number=135,
    set_code="ME2PT5",
    regulation_mark="I",
    rarity=Rarities.RareHoloEX,
    hp=330,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Scraggy.Name",
    family_id=559,
    abilities=[
        Ability(
            title="Counterattacking Crest",
            game_text="If this Pokémon is in the Active Spot and is damaged by an attack from your opponent's Pokémon (even if this Pokémon is Knocked Out), place 5 damage counters on the Attacking Pokémon.",
            effect=standard_ability,
            trigger=Triggers.ON_DAMAGED_BY_ATTACK,
        ),
        Attack(
            title="Outlaw Leg",
            game_text="Discard a random card from your opponent's hand. Discard the top card of your opponent's deck.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=160,
            effect=standard_attack,
        ),
    ],
)
