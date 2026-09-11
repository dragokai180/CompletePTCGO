from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='b17f033e-adc4-52f5-9c6f-f9517feed496',
    key='SV1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Houndstone.Name',
    display_name='Houndstone',
    searchable_by=['Houndstone', 'Stage 1', 'Houndstone'],
    subtypes=['Stage 1'],
    collector_number=106,
    set_code='SV1',
    regulation_mark='G',
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Greavard.Name',
    family_id=971,
    abilities=[
        Attack(
            title='Last Respects',
            game_text='This attack does 10 more damage for each Psychic Pokémon in your discard pile.',
            cost={PokemonTypes.PSYCHIC: 2},
            damage=80,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
