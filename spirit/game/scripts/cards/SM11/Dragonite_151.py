from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='e9c6ae37-5560-504a-ac7c-28f132f36a7f',
    key='SM11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Dragonite.Name',
    display_name='Dragonite',
    searchable_by=['Dragonite', 'Stage 2', 'Dragonite'],
    subtypes=['Stage 2'],
    collector_number=151,
    set_code='SM11',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=160,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FAIRY,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Dragonair.Name',
    family_id=147,
    abilities=[
        Ability(
            title='Hurricane Charge',
            game_text='Once during your turn (before your attack), you may attach a Water Energy card, a Lightning Energy card, or 1 of each from your hand to your Pokémon in any way you like.',
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Dragon Impact',
            game_text='Discard 3 Energy from this Pokémon.',
            cost={PokemonTypes.WATER: 1, PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=170,
            effect=standard_attack,
        ),
    ],
)
