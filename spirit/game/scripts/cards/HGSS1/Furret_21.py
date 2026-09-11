from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='6f147a98-0ecd-50af-a980-86c9ae3fe08f',
    key='HGSS1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Furret.Name',
    display_name='Furret',
    searchable_by=['Furret', 'Stage 1', 'Furret'],
    subtypes=['Stage 1'],
    collector_number=21,
    set_code='HGSS1',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Sentret.Name',
    family_id=161,
    abilities=[
        Attack(
            title='Find a Friend',
            game_text='Search your deck for a Pokémon, show it to your opponent, and put it into your hand. Shuffle your deck afterward.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Quick Blow',
            game_text='Flip a coin. If heads, this attack does 20 damage plus 20 more damage.',
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
