from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='640bec7c-421b-5945-a6cc-b4afdb6f4d50',
    key='SM5',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Weavile.Name',
    display_name='Weavile',
    searchable_by=['Weavile', 'Stage 1', 'Weavile'],
    subtypes=['Stage 1'],
    collector_number=74,
    set_code='SM5',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Sneasel.Name',
    family_id=215,
    abilities=[
        Attack(
            title='Icy Wind',
            game_text="Your opponent's Active Pokémon is now Asleep.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=standard_attack,
        ),
        Attack(
            title='Evil Admonition',
            game_text="This attack does 50 damage for each of your opponent's Pokémon that has an Ability.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=50,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
