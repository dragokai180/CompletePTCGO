from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='29471471-558b-59b3-a8f0-ddca55de7496',
    key='XY1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Delcatty.Name',
    display_name='Delcatty',
    searchable_by=['Delcatty', 'Stage 1', 'Delcatty'],
    subtypes=['Stage 1'],
    collector_number=105,
    set_code='XY1',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Skitty.Name',
    family_id=300,
    abilities=[
        Attack(
            title='Energy Salon',
            game_text='Search your deck for 3 different types of basic Energy cards, reveal them, and put them into your hand. Shuffle your deck afterward.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Fake Out',
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=standard_attack,
        ),
    ],
)
