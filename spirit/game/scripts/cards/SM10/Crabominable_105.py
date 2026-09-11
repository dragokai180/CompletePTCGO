from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='f7557dea-fbcb-5f15-99ee-13238e168dc4',
    key='SM10',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Crabominable.Name',
    display_name='Crabominable',
    searchable_by=['Crabominable', 'Stage 1', 'Crabominable'],
    subtypes=['Stage 1'],
    collector_number=105,
    set_code='SM10',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Crabrawler.Name',
    family_id=739,
    abilities=[
        Attack(
            title='Fight Alone',
            game_text='If you have fewer Pokémon in play than your opponent, this attack does 50 more damage for each Pokémon fewer you have in play.',
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator='+',
            effect=standard_attack,
        ),
        Attack(
            title='Magnum Punch',
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
        ),
    ],
)
