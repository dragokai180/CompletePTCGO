from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='2486334b-02ae-5c1f-966d-d5e1c4f348f7',
    key='Promo_SM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Sudowoodo.Name',
    display_name='Sudowoodo',
    searchable_by=['Sudowoodo', 'Basic', 'Sudowoodo'],
    subtypes=['Basic'],
    collector_number=207,
    set_code='Promo_SM',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=110,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    family_id=185,
    abilities=[
        Attack(
            title='Low Kick',
            cost={PokemonTypes.FIGHTING: 1},
            damage=20,
        ),
        Attack(
            title='Territorial Strike',
            game_text="If you don't have a Stadium card in play, this attack does nothing.",
            cost={PokemonTypes.FIGHTING: 2},
            damage=80,
            effect=standard_attack,
        ),
    ],
)
