from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='89eea6b9-9fa7-568c-b1f7-bf59ebab12a9',
    key='HGSS4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Dragonair.Name',
    display_name='Dragonair',
    searchable_by=['Dragonair', 'Stage 1', 'Dragonair'],
    subtypes=['Stage 1'],
    collector_number=32,
    set_code='HGSS4',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.COLORLESS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Dratini.Name',
    family_id=147,
    abilities=[
        Attack(
            title='Search and Invite',
            game_text='Search your deck for up to 2 Pokémon, show them to your opponent, and put them into your hand. Shuffle your deck afterward.',
            cost={PokemonTypes.COLORLESS: 2},
            effect=standard_attack,
        ),
        Attack(
            title='Slam',
            game_text='Flip 2 coins. This attack does 40 damage times the number of heads.',
            cost={PokemonTypes.COLORLESS: 3},
            damage=40,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
