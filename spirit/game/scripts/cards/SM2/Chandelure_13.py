from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='5172b7b5-9594-54c8-82d6-630375f9fb44',
    key='SM2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Chandelure.Name',
    display_name='Chandelure',
    searchable_by=['Chandelure', 'Stage 2', 'Chandelure'],
    subtypes=['Stage 2'],
    collector_number=13,
    set_code='SM2',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Lampent.Name',
    family_id=607,
    abilities=[
        Ability(
            title='Shady Move',
            game_text='Once during your turn (before your attack), you may move 1 damage counter from 1 Pokémon to another Pokémon.',
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Super Singe',
            game_text="Your opponent's Active Pokémon is now Burned.",
            cost={PokemonTypes.FIRE: 1},
            damage=50,
            effect=standard_attack,
        ),
    ],
)
