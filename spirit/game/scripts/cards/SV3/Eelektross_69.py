from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='ef1c6a9b-7e29-5abc-b226-20d87cf1c5a7',
    key='SV3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Eelektross.Name',
    display_name='Eelektross',
    searchable_by=['Eelektross', 'Stage 2', 'Eelektross'],
    subtypes=['Stage 2'],
    collector_number=69,
    set_code='SV3',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=160,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Eelektrik.Name',
    family_id=602,
    abilities=[
        Attack(
            title='Suction Shock',
            game_text="Switch in 1 of your opponent's Benched Pokémon to the Active Spot. If you do, this attack does 60 damage to the new Active Pokémon, and then flip a coin. If heads, that Pokémon is now Paralyzed.",
            cost={PokemonTypes.LIGHTNING: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Head Bolt',
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=130,
        ),
    ],
)
