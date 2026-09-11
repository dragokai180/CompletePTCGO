from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='c3a6c661-2a50-5994-9a68-05c6a5814732',
    key='XY5',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Starmie.Name',
    display_name='Starmie',
    searchable_by=['Starmie', 'Stage 1', 'Starmie'],
    subtypes=['Stage 1'],
    collector_number=73,
    set_code='XY5',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Staryu.Name',
    family_id=120,
    abilities=[
        Attack(
            title='Synchro Star',
            game_text="If this Pokémon and your opponent's Active Pokémon have the same amount of Energy attached to them, this attack does 60 more damage.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
