from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='6decb528-a0f3-5fdf-8d6a-d44b9e8ca759',
    key='XY7',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Entei.Name',
    display_name='Entei',
    searchable_by=['Entei', 'Basic', 'Entei'],
    subtypes=['Basic'],
    collector_number=14,
    set_code='XY7',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    family_id=244,
    abilities=[
        Attack(
            title='Burning Roar',
            game_text='Discard the top 4 cards of your deck. If any of those cards are Fire Energy cards, attach them to your Pokémon in any way you like.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Combat Blaze',
            game_text="This attack does 20 more damage for each of your opponent's Benched Pokémon.",
            cost={PokemonTypes.FIRE: 2},
            damage=20,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
