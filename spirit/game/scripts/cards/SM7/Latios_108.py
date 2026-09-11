from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='88fd5ede-5c1c-5fc3-a4e4-e0e59433567b',
    key='SM7',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Latios.Name',
    display_name='Latios ◇',
    searchable_by=['Latios ◇', 'Basic', 'Prism Star', 'Latios'],
    subtypes=['Basic', 'Prism Star'],
    collector_number=108,
    set_code='SM7',
    regulation_mark=None,
    rarity=Rarities.Prism,
    hp=140,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FAIRY,
    weakness_amount=2,
    family_id=381,
    abilities=[
        Attack(
            title='Dragon Fleet',
            game_text='This attack does 50 damage for each of your Evolution Dragon Pokémon in play.',
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
