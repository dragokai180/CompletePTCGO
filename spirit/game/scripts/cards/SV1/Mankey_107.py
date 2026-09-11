from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='e5b6bd97-5a47-5f7f-96f2-fb36e49373c8',
    key='SV1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Mankey.Name',
    display_name='Mankey',
    searchable_by=['Mankey', 'Basic', 'Mankey'],
    subtypes=['Basic'],
    collector_number=107,
    set_code='SV1',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=56,
    abilities=[
        Attack(
            title='Monkey Beatdown',
            game_text='This Pokémon also does 10 damage to itself.',
            cost={PokemonTypes.FIGHTING: 1},
            damage=30,
            effect=standard_attack,
        ),
    ],
)
