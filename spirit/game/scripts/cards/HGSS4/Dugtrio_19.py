from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='4df6c696-7bf7-5046-9675-4a5297e47d6a',
    key='HGSS4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Dugtrio.Name',
    display_name='Dugtrio',
    searchable_by=['Dugtrio', 'Stage 1', 'Dugtrio'],
    subtypes=['Stage 1'],
    collector_number=19,
    set_code='HGSS4',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    resistance_type=PokemonTypes.LIGHTNING,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Diglett.Name',
    family_id=50,
    abilities=[
        Attack(
            title='Dig',
            cost={PokemonTypes.FIGHTING: 1},
            damage=30,
        ),
        Attack(
            title='Sand Impact',
            game_text='Flip a coin for each Fighting Energy attached to Dugtrio. This attack does 50 damage plus 20 more damage for each heads.',
            cost={PokemonTypes.COLORLESS: 3},
            damage=50,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
