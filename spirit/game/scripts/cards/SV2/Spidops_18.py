from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='828055c0-8eee-5470-b035-dabbbceeb2d6',
    key='SV2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Spidops.Name',
    display_name='Spidops',
    searchable_by=['Spidops', 'Stage 1', 'Spidops'],
    subtypes=['Stage 1'],
    collector_number=18,
    set_code='SV2',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Tarountula.Name',
    family_id=917,
    abilities=[
        Attack(
            title='Entangling Trap',
            game_text="Shuffle each player's Active Pokémon and all attached cards into their deck.\xa0(You choose a new Active Pokémon first.)",
            cost={PokemonTypes.GRASS: 2},
            effect=standard_attack,
        ),
        Attack(
            title='Hammer In',
            cost={PokemonTypes.GRASS: 3},
            damage=130,
        ),
    ],
)
