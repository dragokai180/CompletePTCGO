from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='a3d4a1d7-629a-56ad-9a17-763a81d48713',
    key='SM10',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Kyurem.Name',
    display_name='Kyurem',
    searchable_by=['Kyurem', 'Basic', 'Kyurem'],
    subtypes=['Basic'],
    collector_number=50,
    set_code='SM10',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    family_id=646,
    abilities=[
        Attack(
            title='Call Forth Cold',
            game_text='Search your deck for a Water Energy card and attach it to this Pokémon. Then, shuffle your deck.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Hail Prison',
            game_text="Discard 2 Water Energy from this Pokémon. Your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=110,
            effect=standard_attack,
        ),
    ],
)
