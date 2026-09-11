from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='f3040a71-7ebc-5339-806a-10340352b4f8',
    key='SM10',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Sandslash.Name',
    display_name='Sandslash',
    searchable_by=['Sandslash', 'Stage 1', 'Sandslash'],
    subtypes=['Stage 1'],
    collector_number=84,
    set_code='SM10',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Sandshrew.Name',
    family_id=27,
    abilities=[
        Attack(
            title='Continuous Scratch',
            game_text='Flip 4 coins. This attack does 30 damage for each heads.',
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator='x',
            effect=standard_attack,
        ),
        Attack(
            title='Sand Tomb',
            game_text="The Defending Pokémon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
            effect=standard_attack,
        ),
    ],
)
