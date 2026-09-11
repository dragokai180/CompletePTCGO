from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='c3f8fc4f-0293-54fb-861c-ea4b1a8e4b51',
    key='SM5',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Hippopotas.Name',
    display_name='Hippopotas',
    searchable_by=['Hippopotas', 'Basic', 'Hippopotas'],
    subtypes=['Basic'],
    collector_number=68,
    set_code='SM5',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=449,
    abilities=[
        Attack(
            title='Eleventh Hour Tackle',
            game_text='If there are 3 or fewer cards in your deck, this attack does 130 more damage.',
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
