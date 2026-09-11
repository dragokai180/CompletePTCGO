from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='4cb50045-5df6-5352-b7f9-6f1ed556d1b5',
    key='HGSS1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Blissey.Name',
    display_name='Blissey',
    searchable_by=['Blissey', 'Stage 1', 'Blissey'],
    subtypes=['Stage 1'],
    collector_number=36,
    set_code='HGSS1',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Chansey.Name',
    family_id=113,
    abilities=[
        Attack(
            title='Energy Link',
            game_text='Search your discard pile for an Energy card and attach it to Blissey.',
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=standard_attack,
        ),
        Attack(
            title='Double-edge',
            game_text='Blissey does 40 damage to itself.',
            cost={PokemonTypes.COLORLESS: 3},
            damage=80,
            effect=standard_attack,
        ),
    ],
)
