from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='9dba04fe-acf1-511e-a108-db90130b078f',
    key='SV4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Absol.Name',
    display_name='Absol',
    searchable_by=['Absol', 'Basic', 'Absol'],
    subtypes=['Basic'],
    collector_number=113,
    set_code='SV4',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=359,
    abilities=[
        Attack(
            title='Drawareness',
            game_text='You may discard any number of cards from your hand until you have 4 or fewer. Draw cards until you have 5 cards in your hand.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Enhanced Blade',
            game_text='If this Pokémon has a Pokémon Tool attached, this attack does 60 more damage.',
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
