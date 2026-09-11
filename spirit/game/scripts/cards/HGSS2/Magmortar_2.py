from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='1cbe3343-9e40-5b07-8e51-6f17582ecf1f',
    key='HGSS2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Magmortar.Name',
    display_name='Magmortar',
    searchable_by=['Magmortar', 'Stage 1', 'Magmortar'],
    subtypes=['Stage 1'],
    collector_number=2,
    set_code='HGSS2',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Magmar.Name',
    family_id=126,
    abilities=[
        Attack(
            title='Hard Crush',
            game_text='Discard the top 3 cards from your deck. This attack does 50 damage times the number of Energy cards you discarded.',
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator='x',
            effect=standard_attack,
        ),
        Attack(
            title='Mantle Bazooka',
            game_text='Discard 2 Fire Energy attached to Magmortar.',
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 2},
            damage=100,
            effect=standard_attack,
        ),
    ],
)
