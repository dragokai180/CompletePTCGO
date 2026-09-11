from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='78e8fadb-5980-5e90-a120-eeb55a6fe1f7',
    key='SM9',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Ninetales.Name',
    display_name='Ninetales',
    searchable_by=['Ninetales', 'Stage 1', 'Ninetales'],
    subtypes=['Stage 1'],
    collector_number=16,
    set_code='SM9',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Vulpix.Name',
    family_id=37,
    abilities=[
        Ability(
            title='Nine Temptations',
            game_text="Once during your turn (before your attack), you may discard 2 Fire Energy cards from your hand. If you do, switch 1 of your opponent's Benched Pokémon with their Active Pokémon.",
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Flame Tail',
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
        ),
    ],
)
