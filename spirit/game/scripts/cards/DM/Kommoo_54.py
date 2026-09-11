from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='f29b8957-fccd-5b55-86b5-5c3d66b28add',
    key='DM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Kommoo.Name',
    display_name='Kommo-o',
    searchable_by=['Kommo-o', 'Stage 2', 'Kommoo'],
    subtypes=['Stage 2'],
    collector_number=54,
    set_code='DM',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=160,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FAIRY,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Hakamoo.Name',
    family_id=782,
    abilities=[
        Attack(
            title='Guard Press',
            game_text="During your opponent's next turn, this Pokémon takes 30 less damage from attacks (after applying Weakness and Resistance).",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
            effect=standard_attack,
        ),
        Attack(
            title='Raging Uppercut',
            game_text='If this Pokémon has 8 or more damage counters on it, this attack does 120 more damage.',
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
