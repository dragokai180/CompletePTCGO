from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='6f97857b-63e5-5c68-b272-8b84b9539a6d',
    key='SM2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Blissey.Name',
    display_name='Blissey',
    searchable_by=['Blissey', 'Stage 1', 'Blissey'],
    subtypes=['Stage 1'],
    collector_number=102,
    set_code='SM2',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=160,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Chansey.Name',
    family_id=113,
    abilities=[
        Ability(
            title='Fresh Egg',
            game_text='When you play this Pokémon from your hand to evolve 1 of your Pokémon during your turn, you may heal 80 damage from your Active Pokémon.',
            effect=standard_ability,
            trigger=Triggers.ON_EVOLVE,
        ),
        Attack(
            title='Double-Edge',
            game_text='This Pokémon does 80 damage to itself.',
            cost={PokemonTypes.COLORLESS: 4},
            damage=160,
            effect=standard_attack,
        ),
    ],
)
