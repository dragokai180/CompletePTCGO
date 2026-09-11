from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='4e72b472-a01e-59a9-b3b3-12dc95b9c9e7',
    key='SM7',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Claydol.Name',
    display_name='Claydol',
    searchable_by=['Claydol', 'Stage 1', 'Claydol'],
    subtypes=['Stage 1'],
    collector_number=79,
    set_code='SM7',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Baltoy.Name',
    family_id=343,
    abilities=[
        Attack(
            title='Psy Bolt',
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=standard_attack,
        ),
        Attack(
            title='Miraculous Spin',
            game_text="This attack does 40 damage for each Steven's Resolve card in your discard pile.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
