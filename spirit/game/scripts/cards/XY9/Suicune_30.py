from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='0962cb18-25b3-524d-b57e-2b3070b87980',
    key='XY9',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Suicune.Name',
    display_name='Suicune',
    searchable_by=['Suicune', 'Basic', 'Suicune'],
    subtypes=['Basic'],
    collector_number=30,
    set_code='XY9',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=245,
    abilities=[
        Ability(
            title='Wind Charm',
            game_text="As long as this Pokémon is your Active Pokémon, prevent all effects of your opponent's attacks, except damage, done to each of your Pokémon. (Existing effects are not removed.)",
            passive=standard_passive("As long as this Pokémon is your Active Pokémon, prevent all effects of your opponent's attacks, except damage, done to each of your Pokémon. (Existing effects are not removed.)"),
        ),
        Attack(
            title='Aurora Beam',
            cost={PokemonTypes.WATER: 3},
            damage=110,
        ),
    ],
)
