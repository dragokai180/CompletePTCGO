from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='9f0d3144-cfb5-5310-b361-868f6c211953',
    key='Promo_XY',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Rayquaza.Name',
    display_name='Rayquaza',
    searchable_by=['Rayquaza', 'Basic', 'Rayquaza'],
    subtypes=['Basic'],
    collector_number=64,
    set_code='Promo_XY',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=120,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FAIRY,
    weakness_amount=2,
    family_id=384,
    abilities=[
        Ability(
            title='Ozone Wall',
            game_text="As long as this Pokémon is on your Bench, prevent all damage done to this Pokémon by attacks (both yours and your opponent's.)",
            passive=standard_passive("As long as this Pokémon is on your Bench, prevent all damage done to this Pokémon by attacks (both yours and your opponent's.)"),
        ),
        Attack(
            title='Dragon Pulse',
            game_text='Discard the top 3 cards of your deck.',
            cost={PokemonTypes.FIRE: 2, PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=130,
            effect=standard_attack,
        ),
    ],
)
