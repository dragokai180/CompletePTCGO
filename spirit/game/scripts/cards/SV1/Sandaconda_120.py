from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='4264f9fe-a02e-53ba-b542-4237a0f9a1ee',
    key='SV1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Sandaconda.Name',
    display_name='Sandaconda',
    searchable_by=['Sandaconda', 'Stage 1', 'Sandaconda'],
    subtypes=['Stage 1'],
    collector_number=120,
    set_code='SV1',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=140,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Silicobra.Name',
    family_id=843,
    abilities=[
        Attack(
            title='Skull Bash',
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
        ),
        Attack(
            title='Sandstorm Spray',
            game_text='Discard 2 Energy from this Pokémon. If you discarded any Energy in this way, your opponent shuffles their Active Pokémon and all attached cards into their deck.',
            cost={PokemonTypes.FIGHTING: 3, PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
    ],
)
