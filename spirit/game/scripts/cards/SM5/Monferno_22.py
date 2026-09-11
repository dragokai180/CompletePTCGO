from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='7cebbf17-86e7-5464-87e8-38b479fa40f4',
    key='SM5',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Monferno.Name',
    display_name='Monferno',
    searchable_by=['Monferno', 'Stage 1', 'Monferno'],
    subtypes=['Stage 1'],
    collector_number=22,
    set_code='SM5',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Chimchar.Name',
    family_id=390,
    abilities=[
        Attack(
            title='Super Singe',
            game_text="Your opponent's Active Pokémon is now Burned.",
            cost={PokemonTypes.FIRE: 1},
            damage=20,
            effect=standard_attack,
        ),
    ],
)
