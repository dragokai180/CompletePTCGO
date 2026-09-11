from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='ba18604d-328a-5e4e-8acc-132c098ec5ee',
    key='XY7',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Volcarona.Name',
    display_name='Volcarona',
    searchable_by=['Volcarona', 'Stage 1', 'Volcarona'],
    subtypes=['Stage 1'],
    collector_number=17,
    set_code='XY7',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Larvesta.Name',
    family_id=636,
    abilities=[
        Attack(
            title='Solar Birth',
            game_text='Search your deck for a Basic Pokémon and put it onto your Bench. Then, search your deck for up to 2 basic Energy cards and attach them to that Pokémon. Shuffle your deck afterward.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Flamethrower',
            game_text='Discard an Energy attached to this Pokémon.',
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
            effect=standard_attack,
        ),
    ],
)
