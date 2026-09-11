from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='462e5a99-1a96-5288-8691-7d6babcec073',
    key='HGSS4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Lairon.Name',
    display_name='Lairon',
    searchable_by=['Lairon', 'Stage 1', 'Lairon'],
    subtypes=['Stage 1'],
    collector_number=37,
    set_code='HGSS4',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Aron.Name',
    family_id=304,
    abilities=[
        Attack(
            title='Take Down',
            game_text='Lairon does 20 damage to itself.',
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
            effect=standard_attack,
        ),
    ],
)
