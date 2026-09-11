from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='f6adc6c9-f6cc-5c77-b3e0-5ab8575ef385',
    key='HGSS4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Aggron.Name',
    display_name='Aggron',
    searchable_by=['Aggron', 'Stage 2', 'Aggron'],
    subtypes=['Stage 2'],
    collector_number=1,
    set_code='HGSS4',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Lairon.Name',
    family_id=304,
    abilities=[
        Attack(
            title='Second Strike',
            game_text='If the Defending Pokémon already has any damage counters on it, this attack does 40 damage plus 40 more damage.',
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=standard_attack,
        ),
        Attack(
            title='Guard Claw',
            game_text="During your opponent's next turn, any damage done to Aggron by attacks is reduced by 20 (after applying Weakness and Resistance).",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=standard_attack,
        ),
    ],
)
