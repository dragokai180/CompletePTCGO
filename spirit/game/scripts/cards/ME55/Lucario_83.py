from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='4d40104f-5277-574d-ada8-f49e2c036ff6',
    key='ME55',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Lucario.Name',
    display_name='Lucario',
    searchable_by=['Lucario', 'Stage 1', 'Lucario'],
    subtypes=['Stage 1'],
    collector_number=83,
    set_code='ME55',
    regulation_mark='J',
    rarity=Rarities.Common,
    hp=120,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Riolu.Name',
    family_id=448,
    abilities=[
        Attack(
            title='Aura Sphere',
            game_text="This attack also does 60 damage to 1 of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
            effect=standard_attack,
        ),
    ],
)

from spirit.game.card_effects.thirtieth_celebration import configure
configure(card)
