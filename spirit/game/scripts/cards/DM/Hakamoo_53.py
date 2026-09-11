from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='ea885a69-5e16-5ba6-8a63-3880f5bc4703',
    key='DM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Hakamoo.Name',
    display_name='Hakamo-o',
    searchable_by=['Hakamo-o', 'Stage 1', 'Hakamoo'],
    subtypes=['Stage 1'],
    collector_number=53,
    set_code='DM',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FAIRY,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Jangmoo.Name',
    family_id=782,
    abilities=[
        Attack(
            title='Guard Press',
            game_text="During your opponent's next turn, this Pokémon takes 30 less damage from attacks (after applying Weakness and Resistance).",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=standard_attack,
        ),
        Attack(
            title='Dragon Claw',
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=70,
        ),
    ],
)
