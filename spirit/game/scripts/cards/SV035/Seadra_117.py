from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='fa9335b9-a86c-5a6b-9564-3199303c9c4d',
    key='SV035',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Seadra.Name',
    display_name='Seadra',
    searchable_by=['Seadra', 'Stage 1', 'Seadra'],
    subtypes=['Stage 1'],
    collector_number=117,
    set_code='SV035',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Horsea.Name',
    family_id=116,
    abilities=[
        Attack(
            title='Blinding Ink',
            game_text="During your opponent's next turn, if the Defending Pokémon tries to use an attack, your opponent flips 2 coins. If either of them is tails, that attack doesn't happen.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=standard_attack,
        ),
    ],
)
