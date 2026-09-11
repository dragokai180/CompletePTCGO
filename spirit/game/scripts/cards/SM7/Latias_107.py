from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='ed5d024d-0e2c-5d1c-bde9-540046b533a4',
    key='SM7',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Latias.Name',
    display_name='Latias ◇',
    searchable_by=['Latias ◇', 'Basic', 'Prism Star', 'Latias'],
    subtypes=['Basic', 'Prism Star'],
    collector_number=107,
    set_code='SM7',
    regulation_mark=None,
    rarity=Rarities.Prism,
    hp=130,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FAIRY,
    weakness_amount=2,
    family_id=380,
    abilities=[
        Attack(
            title='Dreamy Mist',
            game_text='Attach a basic Energy card from your discard pile to each of your Basic Benched Dragon Pokémon.',
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=standard_attack,
        ),
    ],
)
