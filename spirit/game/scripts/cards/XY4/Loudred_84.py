from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='a3cb8176-6b89-5be4-ab0b-3a003ee9cfa5',
    key='XY4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Loudred.Name',
    display_name='Loudred',
    searchable_by=['Loudred', 'Stage 1', 'Loudred'],
    subtypes=['Stage 1'],
    collector_number=84,
    set_code='XY4',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Whismur.Name',
    family_id=293,
    abilities=[
        Attack(
            title='Pound',
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
        Attack(
            title='Energy Press',
            game_text="This attack does 30 more damage for each Energy attached to your opponent's Active Pokémon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
