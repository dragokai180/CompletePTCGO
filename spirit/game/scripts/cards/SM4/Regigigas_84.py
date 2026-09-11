from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='971f3507-0cac-50dd-85fb-5d9e8ce52ade',
    key='SM4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Regigigas.Name',
    display_name='Regigigas',
    searchable_by=['Regigigas', 'Basic', 'Regigigas'],
    subtypes=['Basic'],
    collector_number=84,
    set_code='SM4',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=180,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=486,
    abilities=[
        Ability(
            title='Seal of Antiquity',
            game_text="This Pokémon can't attack unless Regirock, Regice, and Registeel are on your Bench.",
            passive=standard_passive("This Pokémon can't attack unless Regirock, Regice, and Registeel are on your Bench."),
        ),
        Attack(
            title='Giant Stomp',
            game_text='Discard any Stadium card in play.',
            cost={PokemonTypes.COLORLESS: 5},
            damage=160,
            effect=standard_attack,
        ),
    ],
)
