from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='ea310bb7-e045-55c5-a408-d5b37ecfbc02',
    key='TATM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.TeamAquasSharpedo.Name',
    display_name="Team Aqua's Sharpedo",
    searchable_by=["Team Aqua's Sharpedo", 'Stage 1', 'TeamAquasSharpedo'],
    subtypes=['Stage 1'],
    collector_number=21,
    set_code='TATM',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.TeamAquasCarvanha.Name',
    family_id=318,
    abilities=[
        Ability(
            title='Aqua Search',
            game_text='Once during your turn (before your attack), you may search your deck for a Team Aqua Pokémon, reveal it, and put it into your hand. Shuffle your deck afterward.',
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Sharp Fang',
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
        ),
    ],
)
