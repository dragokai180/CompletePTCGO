from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='0afcdef9-7620-590e-90fc-da2355708b9c',
    key='HGSS2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Lucario.Name',
    display_name='Lucario',
    searchable_by=['Lucario', 'Stage 1', 'Lucario'],
    subtypes=['Stage 1'],
    collector_number=19,
    set_code='HGSS2',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Riolu.Name',
    family_id=447,
    abilities=[
        Attack(
            title='Bulk Up',
            game_text="During your next turn, each of Lucario's attacks does 30 more damage to the Defending Pokémon (before applying Weakness and Resistance).",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=standard_attack,
        ),
        Attack(
            title='Magnum Punch',
            cost={PokemonTypes.FIGHTING: 2},
            damage=50,
        ),
    ],
)
