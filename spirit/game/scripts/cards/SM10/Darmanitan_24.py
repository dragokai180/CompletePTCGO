from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='8ffdd970-f2d4-5a1c-b80c-6d0eda9f97cf',
    key='SM10',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Darmanitan.Name',
    display_name='Darmanitan',
    searchable_by=['Darmanitan', 'Stage 1', 'Darmanitan'],
    subtypes=['Stage 1'],
    collector_number=24,
    set_code='SM10',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Darumaka.Name',
    family_id=554,
    abilities=[
        Attack(
            title='Find Wildfire',
            game_text='Search your deck for up to 3 Fire Energy cards, reveal them, and put them into your hand. Then, shuffle your deck.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Flare Blitz',
            game_text='Discard all Fire Energy from this Pokémon.',
            cost={PokemonTypes.FIRE: 2},
            damage=110,
            effect=standard_attack,
        ),
    ],
)
