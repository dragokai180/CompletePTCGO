from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='b5c3de25-efd1-53e3-ad19-410d2db21b46',
    key='SV035',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Weezing.Name',
    display_name='Weezing',
    searchable_by=['Weezing', 'Stage 1', 'Weezing'],
    subtypes=['Stage 1'],
    collector_number=110,
    set_code='SV035',
    regulation_mark='G',
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Koffing.Name',
    family_id=109,
    abilities=[
        Ability(
            title="Let's Have a Blast",
            game_text="If this Pokémon is in the Active Spot and is Knocked Out by damage from an attack from your opponent's Pokémon, flip a coin. If heads, the Attacking Pokémon is Knocked Out.",
            passive=standard_passive("If this Pokémon is in the Active Spot and is Knocked Out by damage from an attack from your opponent's Pokémon, flip a coin. If heads, the Attacking Pokémon is Knocked Out."),
        ),
        Attack(
            title='Spinning Fumes',
            game_text="This attack also does 10 damage to each of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=standard_attack,
        ),
    ],
)
