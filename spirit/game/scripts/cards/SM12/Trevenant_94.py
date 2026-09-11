from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='e7873c60-5a14-59d1-8115-1a54b1a4dd38',
    key='SM12',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Trevenant.Name',
    display_name='Trevenant',
    searchable_by=['Trevenant', 'Stage 1', 'Trevenant'],
    subtypes=['Stage 1'],
    collector_number=94,
    set_code='SM12',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Phantump.Name',
    family_id=708,
    abilities=[
        Attack(
            title='Perplexing Forest',
            game_text='You may have your opponent switch their Active Pokémon with 1 of their Benched Pokémon.',
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=standard_attack,
        ),
        Attack(
            title='Shadow Impact',
            game_text='Put 4 damage counters on 1 of your Pokémon.',
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=120,
            effect=standard_attack,
        ),
    ],
)
