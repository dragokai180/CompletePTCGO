from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='848010e0-9d4f-5e22-9f1b-9b634779741e',
    key='HGSS4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Spoink.Name',
    display_name='Spoink',
    searchable_by=['Spoink', 'Basic', 'Spoink'],
    subtypes=['Basic'],
    collector_number=77,
    set_code='HGSS4',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=325,
    abilities=[
        Attack(
            title='Sleep Pearl',
            game_text='The Defending Pokémon is now Asleep. Switch Spoink with 1 of your Benched Pokémon.',
            cost={PokemonTypes.PSYCHIC: 1},
            effect=standard_attack,
        ),
    ],
)
